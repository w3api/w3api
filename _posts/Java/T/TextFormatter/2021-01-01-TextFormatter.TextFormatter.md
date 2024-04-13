---
title: TextFormatter.TextFormatter()
permalink: /Java/TextFormatter/TextFormatter/
date: 2021-01-11
key: Java.T.TextFormatter
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextFormatter.constructores valor="TextFormatter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TextFormatter(UnaryOperator<TextFormatter.Change> filter)
public TextFormatter(StringConverter<V> valueConverter)
public TextFormatter(StringConverter<V> valueConverter, V defaultValue)
public TextFormatter(StringConverter<V> valueConverter, V defaultValue, UnaryOperator<TextFormatter.Change> filter)
~~~

## Parámetros
* **StringConverter&lt;V&gt; valueConverter**,  {% include w3api/param_description.html metodo=_dato parametro="StringConverter<V> valueConverter" %}
* **V defaultValue**,  {% include w3api/param_description.html metodo=_dato parametro="V defaultValue" %}
* **UnaryOperator&lt;TextFormatter.Change&gt; filter**,  {% include w3api/param_description.html metodo=_dato parametro="UnaryOperator<TextFormatter.Change> filter" %}

## Clase Padre
[TextFormatter](/Java/TextFormatter/)

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
