---
title: StyleConverter.convert()
permalink: Java/StyleConverter/convert
date: 2021-01-11
key: JavaJava.S.StyleConverter
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleConverter.metodos valor="convert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public T convert(Map<CssMetaData<? extends Styleable,?>,Object> convertedValues)
public T convert(ParsedValue<F,T> value, Font font)
~~~

## Parámetros
* **Object&gt; convertedValues**,  {% include w3api/param_description.html metodo=_dato parametro="Object> convertedValues" %}
* **T&gt; value**,  {% include w3api/param_description.html metodo=_dato parametro="T> value" %}
* **Map&lt;CssMetaData&lt;? extends Styleable**,  {% include w3api/param_description.html metodo=_dato parametro="Map<CssMetaData<? extends Styleable" %}
* **Font font**,  {% include w3api/param_description.html metodo=_dato parametro="Font font" %}
* **ParsedValue&lt;F**,  {% include w3api/param_description.html metodo=_dato parametro="ParsedValue<F" %}
* **?&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="?>" %}

## Clase Padre
[StyleConverter](/Java/StyleConverter/)

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
