---
title: StyleConverter.convert()
permalink: Java/StyleConverter/convert
date: 2021-01-04
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
* **T&gt; value**,  {% include w3api/param_description.html metodo=_data parametro="T> value" %}
* **Map&lt;CssMetaData&lt;? extends Styleable**,  {% include w3api/param_description.html metodo=_data parametro="Map<CssMetaData<? extends Styleable" %}
* **Object&gt; convertedValues**,  {% include w3api/param_description.html metodo=_data parametro="Object> convertedValues" %}
* **ParsedValue&lt;F**,  {% include w3api/param_description.html metodo=_data parametro="ParsedValue<F" %}
* **Font font**,  {% include w3api/param_description.html metodo=_data parametro="Font font" %}
* **?&gt;**,  {% include w3api/param_description.html metodo=_data parametro="?>" %}

## Clase Padre
[StyleConverter](/Java/StyleConverter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StyleConverter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
