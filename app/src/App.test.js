import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react', () => {
  render(<App />);
  const linkElement = screen.getByText(/MTA is presenting this/i);
  expect(linkElement).toBeInTheDocument();
});
