---
title: StyleablePropertyFactory.createStyleableFontProperty()
permalink: Java/StyleablePropertyFactory/createStyleableFontProperty
date: 2021-01-04
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
* **String cssProperty**,  {% include w3api/param_description.html metodo=_data parametro="String cssProperty" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **StyleableProperty&lt;Font&gt;&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="StyleableProperty<Font>> function" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **Font initialValue**,  {% include w3api/param_description.html metodo=_data parametro="Font initialValue" %}
* **S styleable**,  {% include w3api/param_description.html metodo=_data parametro="S styleable" %}

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
{%- for _ldc in site.data.Java.S.StyleablePropertyFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
