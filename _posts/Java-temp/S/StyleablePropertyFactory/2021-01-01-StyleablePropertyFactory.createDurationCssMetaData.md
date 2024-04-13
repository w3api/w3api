---
title: StyleablePropertyFactory.createDurationCssMetaData()
permalink: /Java/StyleablePropertyFactory/createDurationCssMetaData/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createDurationCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CssMetaData<S,Duration> createDurationCssMetaData(String property, Function<S,StyleableProperty<Duration>> function)
public final CssMetaData<S,Duration> createDurationCssMetaData(String property, Function<S,StyleableProperty<Duration>> function, Duration initialValue)
public final CssMetaData<S,Duration> createDurationCssMetaData(String property, Function<S,StyleableProperty<Duration>> function, Duration initialValue, boolean inherits)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **Duration initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Duration initialValue" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}
* **StyleableProperty&lt;Duration&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Duration>> function" %}

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
