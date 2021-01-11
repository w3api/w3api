---
title: StyleablePropertyFactory.createStyleableFontProperty()
permalink: Java/StyleablePropertyFactory/createStyleableFontProperty
date: 2021-01-11
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleableFontProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StyleableProperty<Font> createStyleableFontProperty(S styleable, String propertyName, String cssProperty)
public final StyleableProperty<Font> createStyleableFontProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Font>> function)
public final StyleableProperty<Font> createStyleableFontProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Font>> function, Font initialValue)
public final StyleableProperty<Font> createStyleableFontProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Font>> function, Font initialValue, boolean inherits)
~~~

## Parámetros
* **String cssProperty**,  {% include w3api/param_description.html metodo=_dato parametro="String cssProperty" %}
* **Font initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Font initialValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **StyleableProperty&lt;Font&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Font>> function" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}
* **S styleable**,  {% include w3api/param_description.html metodo=_dato parametro="S styleable" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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