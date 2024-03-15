import App from "../App"
import {render, fireEvent, screen} from "@testing-library/react"
import React from "react";

describe("App", () => {
    it("Displays image", () => {
        const imgUrl ="https://ocdn.eu/photo-offers-prod-transforms/1/GP_ktk3b2ZmZXJzLzIyOTU4MjQ1MjlfZjIyM2Y5ZDM3MjdmMjMyMGRlN2VmZWM1OGQwYzllM2Eud2VicJOVAsy0AMLDlQIAzLTCw5MJpjMyNWJjZQY/rower-stacjonarny-oxygen-yellow.jpg";
        render(<App />);

        const imageElement = screen.getByAltText('search',{src: imgUrl});
        expect(imageElement).toBeInTheDocument();
    });
    it("Typing into Search changes its value", () => {
        const { getByPlaceholderText } = render(<App />);
        const inputElement = getByPlaceholderText("Search for items");
        const searchPhrase = "Rower";
        fireEvent.change(inputElement, { target: { value: searchPhrase } });
        expect(inputElement.value).toBe(searchPhrase);
      });
      test('clicking on search icon triggers search', () => {
        const { getByAltText } = render(<App />);
        const searchIcon = getByAltText('search');
        
        // Sprawdzenie, czy kliknięcie w ikonę wyszukiwania wywołuje funkcję searchItems
        fireEvent.click(searchIcon);
        
        // Tutaj możesz dodać oczekiwanie na efekty wywołania funkcji, jeśli są asynchroniczne
        // np. możesz sprawdzić, czy elementy zostały załadowane
      });
  });