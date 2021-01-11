---
title: StyleablePropertyFactory.createSizeCssMetaData()
permalink: Java/StyleablePropertyFactory/createSizeCssMetaData
date: 2021-01-11
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createSizeCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CssMetaData<S,Number> createSizeCssMetaData(String property, Function<S,StyleableProperty<Number>> function)
public final CssMetaData<S,Number> createSizeCssMetaData(String property, Function<S,StyleableProperty<Number>> function, Number initialValue)
public final CssMetaData<S,Number> createSizeCssMetaData(String property, Function<S,StyleableProperty<Number>> function, Number initialValue, boolean inherits)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **StyleableProperty&lt;Number&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Number>> function" %}
* **Number initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Number initialValue" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
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