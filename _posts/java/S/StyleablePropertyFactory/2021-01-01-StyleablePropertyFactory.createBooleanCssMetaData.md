---
title: StyleablePropertyFactory.createBooleanCssMetaData()
permalink: Java/StyleablePropertyFactory/createBooleanCssMetaData
date: 2021-01-11
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createBooleanCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CssMetaData<S,Boolean> createBooleanCssMetaData(String property, Function<S,StyleableProperty<Boolean>> function)
public final CssMetaData<S,Boolean> createBooleanCssMetaData(String property, Function<S,StyleableProperty<Boolean>> function, boolean initialValue)
public final CssMetaData<S,Boolean> createBooleanCssMetaData(String property, Function<S,StyleableProperty<Boolean>> function, boolean initialValue, boolean inherits)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **boolean initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="boolean initialValue" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}
* **StyleableProperty&lt;Boolean&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Boolean>> function" %}

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
