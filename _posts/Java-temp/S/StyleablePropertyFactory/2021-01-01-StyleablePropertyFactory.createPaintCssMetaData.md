---
title: StyleablePropertyFactory.createPaintCssMetaData()
permalink: /Java/StyleablePropertyFactory/createPaintCssMetaData/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createPaintCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CssMetaData<S,Paint> createPaintCssMetaData(String property, Function<S,StyleableProperty<Paint>> function)
public final CssMetaData<S,Paint> createPaintCssMetaData(String property, Function<S,StyleableProperty<Paint>> function, Paint initialValue)
public final CssMetaData<S,Paint> createPaintCssMetaData(String property, Function<S,StyleableProperty<Paint>> function, Paint initialValue, boolean inherits)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **Paint initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Paint initialValue" %}
* **StyleableProperty&lt;Paint&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Paint>> function" %}
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
