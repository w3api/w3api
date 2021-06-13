---
title: InputMethodContext.dispatchInputMethodEvent()
permalink: /Java/InputMethodContext/dispatchInputMethodEvent/
date: 2021-01-11
key: Java.I.InputMethodContext
category: Java
tags: ['java se', 'java.awt.im.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputMethodContext.metodos valor="dispatchInputMethodEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void dispatchInputMethodEvent(int id, AttributedCharacterIterator text, int committedCharacterCount, TextHitInfo caret, TextHitInfo visiblePosition)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator text" %}
* **TextHitInfo visiblePosition**,  {% include w3api/param_description.html metodo=_dato parametro="TextHitInfo visiblePosition" %}
* **TextHitInfo caret**,  {% include w3api/param_description.html metodo=_dato parametro="TextHitInfo caret" %}
* **int committedCharacterCount**,  {% include w3api/param_description.html metodo=_dato parametro="int committedCharacterCount" %}

## Clase Padre
[InputMethodContext](/Java/InputMethodContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
