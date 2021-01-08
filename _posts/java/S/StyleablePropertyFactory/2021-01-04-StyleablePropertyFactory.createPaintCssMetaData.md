---
title: StyleablePropertyFactory.createPaintCssMetaData()
permalink: Java/StyleablePropertyFactory/createPaintCssMetaData
date: 2021-01-04
key: JavaJava.S.StyleablePropertyFactory
category: java
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
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **StyleableProperty&lt;Paint&gt;&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="StyleableProperty<Paint>> function" %}
* **Paint initialValue**,  {% include w3api/param_description.html metodo=_data parametro="Paint initialValue" %}
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
