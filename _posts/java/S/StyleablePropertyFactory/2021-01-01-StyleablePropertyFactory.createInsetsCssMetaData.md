---
title: StyleablePropertyFactory.createInsetsCssMetaData()
permalink: /Java/StyleablePropertyFactory/createInsetsCssMetaData/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createInsetsCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CssMetaData<S,Insets> createInsetsCssMetaData(String property, Function<S,StyleableProperty<Insets>> function)
public final CssMetaData<S,Insets> createInsetsCssMetaData(String property, Function<S,StyleableProperty<Insets>> function, Insets initialValue)
public final CssMetaData<S,Insets> createInsetsCssMetaData(String property, Function<S,StyleableProperty<Insets>> function, Insets initialValue, boolean inherits)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **Insets initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Insets initialValue" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **StyleableProperty&lt;Insets&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Insets>> function" %}
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
