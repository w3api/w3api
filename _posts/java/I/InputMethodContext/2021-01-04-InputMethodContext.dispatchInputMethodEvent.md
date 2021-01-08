---
title: InputMethodContext.dispatchInputMethodEvent()
permalink: Java/InputMethodContext/dispatchInputMethodEvent
date: 2021-01-04
key: JavaJava.I.InputMethodContext
category: java
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
* **TextHitInfo visiblePosition**,  {% include w3api/param_description.html metodo=_data parametro="TextHitInfo visiblePosition" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **TextHitInfo caret**,  {% include w3api/param_description.html metodo=_data parametro="TextHitInfo caret" %}
* **int committedCharacterCount**,  {% include w3api/param_description.html metodo=_data parametro="int committedCharacterCount" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator text" %}

## Clase Padre
[InputMethodContext](/Java/InputMethodContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InputMethodContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
