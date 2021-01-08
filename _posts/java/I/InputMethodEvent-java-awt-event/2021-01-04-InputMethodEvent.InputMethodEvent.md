---
title: InputMethodEvent.InputMethodEvent()
permalink: Java/InputMethodEvent-java-awt-event/InputMethodEvent
date: 2021-01-04
key: JavaJava.I.InputMethodEvent-java-awt-event
category: java
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
* **TextHitInfo visiblePosition**,  {% include w3api/param_description.html metodo=_data parametro="TextHitInfo visiblePosition" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **TextHitInfo caret**,  {% include w3api/param_description.html metodo=_data parametro="TextHitInfo caret" %}
* **Component source**,  {% include w3api/param_description.html metodo=_data parametro="Component source" %}
* **long when**,  {% include w3api/param_description.html metodo=_data parametro="long when" %}
* **int committedCharacterCount**,  {% include w3api/param_description.html metodo=_data parametro="int committedCharacterCount" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator text" %}

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
{%- for _ldc in site.data.Java.I.InputMethodEvent-java-awt-event.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
