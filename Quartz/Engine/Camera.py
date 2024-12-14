""" Handles the Camera for rendering Frame's """
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Quartz.Engine.Frame import Frame
    from Quartz.Engine.Geometry import Vec2

class Camera:
    """ Object to handle rendering Frame's """

    __slots__ = "frame", "position", "scale", "border"

    def __init__(
        self,
        frame: "Frame",
        position: "Vec2",
        scale: "Vec2",
        border: str = None
    ):
        self.frame = frame
        self.position = position
        self.scale = scale
        self.border = border

    def render(self):
        """Renders the Frame and Pixels inside of it, selecting the highest layer pixel per position."""
        # Calculate half the scale
        half_width = self.scale.x // 2
        half_height = self.scale.y // 2

        # Calculate rendering bounds
        start_x = self.position.x - half_width
        end_x = self.position.x + half_width
        start_y = self.position.y - half_height
        end_y = self.position.y + half_height

        # Get pixel positions from the frame
        pixel_positions = self.frame.get_pixels_position()  # {Vec2: [Pixel]}
        pixel_and_child_positions = self.frame.get_pixels_position()

        for position, pixels in pixel_positions.items():
            for pixel in pixels:
                if pixel.type == "Parent":
                    for child_pixel in pixel.children_pixels:
                        if pixel_and_child_positions.get(child_pixel.position):
                            pixel_and_child_positions[child_pixel.position].add(child_pixel)
                        else:
                            pixel_and_child_positions[child_pixel.position] = {child_pixel}

        render_buffer = []

        # Apply the top border if set
        if self.border is not None:
            render_buffer.append(self.border * (self.scale.x + 3))  # Top border

        # Render the selected area
        for y in range(start_y, end_y + 1):
            row = []
            if self.border is not None:
                row.append(self.border)  # Left border
            for x in range(start_x, end_x + 1):
                # Determine the highest layer pixel at this position
                highest_layer_pixel = max(
                    (
                        pixel
                        for position, pixels in pixel_and_child_positions.items()
                        for pixel in pixels
                        if position.x == x and position.y == y
                    ),
                    key=lambda p: p.layer,
                    default=None,
                )

                if highest_layer_pixel:
                    row.append(highest_layer_pixel.texture)
                else:
                    # Render the backdrop if no pixel matches
                    row.append(self.frame.backdrop)
            if self.border is not None:
                row.append(self.border)  # Right border
            render_buffer.append("".join(row))

        # Apply the bottom border if set
        if self.border is not None:
            render_buffer.append(self.border * (self.scale.x + 3))

        # Print the render buffer
        print("\n".join(render_buffer))
