---
title: StyleablePropertyFactory.createStyleableNumberProperty()
permalink: /Java/StyleablePropertyFactory/createStyleableNumberProperty/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleableNumberProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StyleableProperty<Number> createStyleableNumberProperty(S styleable, String propertyName, String cssProperty)
public final StyleableProperty<Number> createStyleableNumberProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Number>> function)
public final StyleableProperty<Number> createStyleableNumberProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Number>> function, Number initialValue)
public final StyleableProperty<Number> createStyleableNumberProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Number>> function, Number initialValue, boolean inherits)
~~~

## Parámetros
* **StyleableProperty&lt;Number&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Number>> function" %}
* **String cssProperty**,  {% include w3api/param_description.html metodo=_dato parametro="String cssProperty" %}
* **Number initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Number initialValue" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
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
