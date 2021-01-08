---
title: CssMetaData.CssMetaData()
permalink: Java/CssMetaData/CssMetaData
date: 2021-01-04
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
* **V&gt; converter**,  {% include w3api/param_description.html metodo=_data parametro="V> converter" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **StyleConverter&lt;?**,  {% include w3api/param_description.html metodo=_data parametro="StyleConverter<?" %}
* **List&lt;CssMetaData&lt;? extends Styleable**,  {% include w3api/param_description.html metodo=_data parametro="List<CssMetaData<? extends Styleable" %}
* **?&gt;&gt; subProperties**,  {% include w3api/param_description.html metodo=_data parametro="?>> subProperties" %}
* **String property**,  {% include w3api/param_description.html metodo=_data parametro="String property" %}
* **V initialValue**,  {% include w3api/param_description.html metodo=_data parametro="V initialValue" %}

## Clase Padre
[CssMetaData](/Java/CssMetaData/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CssMetaData.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
