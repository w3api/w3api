---
title: StyleablePropertyFactory.createSizeCssMetaData()
permalink: Java/StyleablePropertyFactory/createSizeCssMetaData
date: 2021-01-04
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
* **StyleableProperty&lt;Number&gt;&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="StyleableProperty<Number>> function" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **Number initialValue**,  {% include w3api/param_description.html metodo=_data parametro="Number initialValue" %}
* **String property**,  {% include w3api/param_description.html metodo=_data parametro="String property" %}

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
{%- for _ldc in site.data.Java.S.StyleablePropertyFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
