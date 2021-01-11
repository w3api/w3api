---
title: CssMetaData.CssMetaData()
permalink: Java/CssMetaData/CssMetaData
date: 2021-01-11
key: JavaJava.C.CssMetaData
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CssMetaData.constructores valor="CssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CssMetaData(String property, StyleConverter<?,V> converter)
protected CssMetaData(String property, StyleConverter<?,V> converter, V initialValue)
protected CssMetaData(String property, StyleConverter<?,V> converter, V initialValue, boolean inherits)
protected CssMetaData(String property, StyleConverter<?,V> converter, V initialValue, boolean inherits, List<CssMetaData<? extends Styleable,?>> subProperties)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **StyleConverter&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="StyleConverter<?" %}
* **?&gt;&gt; subProperties**,  {% include w3api/param_description.html metodo=_dato parametro="?>> subProperties" %}
* **V initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="V initialValue" %}
* **List&lt;CssMetaData&lt;? extends Styleable**,  {% include w3api/param_description.html metodo=_dato parametro="List<CssMetaData<? extends Styleable" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **V&gt; converter**,  {% include w3api/param_description.html metodo=_dato parametro="V> converter" %}

## Clase Padre
[CssMetaData](/Java/CssMetaData/)

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
