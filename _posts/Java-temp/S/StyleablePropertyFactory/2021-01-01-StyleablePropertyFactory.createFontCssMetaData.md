---
title: StyleablePropertyFactory.createFontCssMetaData()
permalink: /Java/StyleablePropertyFactory/createFontCssMetaData/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createFontCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CssMetaData<S,Font> createFontCssMetaData(String property, Function<S,StyleableProperty<Font>> function)
public final CssMetaData<S,Font> createFontCssMetaData(String property, Function<S,StyleableProperty<Font>> function, Font initialValue)
public final CssMetaData<S,Font> createFontCssMetaData(String property, Function<S,StyleableProperty<Font>> function, Font initialValue, boolean inherits)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **Font initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Font initialValue" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **StyleableProperty&lt;Font&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Font>> function" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StyleablePropertyFactory](/Java/StyleablePropertyFactory/)

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
