---
title: StyleablePropertyFactory.createUrlCssMetaData()
permalink: /Java/StyleablePropertyFactory/createUrlCssMetaData/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createUrlCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CssMetaData<S,String> createUrlCssMetaData(String property, Function<S,StyleableProperty<String>> function)
public final CssMetaData<S,String> createUrlCssMetaData(String property, Function<S,StyleableProperty<String>> function, String initialValue)
public final CssMetaData<S,String> createUrlCssMetaData(String property, Function<S,StyleableProperty<String>> function, String initialValue, boolean inherits)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **StyleableProperty&lt;String&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<String>> function" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}
* **String initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="String initialValue" %}

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
