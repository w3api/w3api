---
title: InputMethodEvent.InputMethodEvent()
permalink: /Java/InputMethodEvent-java-awt-event/InputMethodEvent/
date: 2021-01-11
key: Java.I.InputMethodEvent-java-awt-event
category: Java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputMethodEvent-java-awt-event.constructores valor="InputMethodEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputMethodEvent(Component source, int id, long when, AttributedCharacterIterator text, int committedCharacterCount, TextHitInfo caret, TextHitInfo visiblePosition)
public InputMethodEvent(Component source, int id, TextHitInfo caret, TextHitInfo visiblePosition)
public InputMethodEvent(Component source, int id, AttributedCharacterIterator text, int committedCharacterCount, TextHitInfo caret, TextHitInfo visiblePosition)
~~~

## Parámetros
* **long when**,  {% include w3api/param_description.html metodo=_dato parametro="long when" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator text" %}
* **TextHitInfo visiblePosition**,  {% include w3api/param_description.html metodo=_dato parametro="TextHitInfo visiblePosition" %}
* **TextHitInfo caret**,  {% include w3api/param_description.html metodo=_dato parametro="TextHitInfo caret" %}
* **int committedCharacterCount**,  {% include w3api/param_description.html metodo=_dato parametro="int committedCharacterCount" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InputMethodEvent](/Java/InputMethodEvent-java-awt-event/)

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
