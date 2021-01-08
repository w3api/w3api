---
title: StyleablePropertyFactory.createInsetsCssMetaData()
permalink: Java/StyleablePropertyFactory/createInsetsCssMetaData
date: 2021-01-04
key: JavaJava.S.StyleablePropertyFactory
category: java
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
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **StyleableProperty&lt;Insets&gt;&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="StyleableProperty<Insets>> function" %}
* **String property**,  {% include w3api/param_description.html metodo=_data parametro="String property" %}
* **Insets initialValue**,  {% include w3api/param_description.html metodo=_data parametro="Insets initialValue" %}

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
