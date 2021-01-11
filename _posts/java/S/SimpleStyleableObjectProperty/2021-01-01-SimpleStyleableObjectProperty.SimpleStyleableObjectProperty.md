---
title: SimpleStyleableObjectProperty.SimpleStyleableObjectProperty()
permalink: Java/SimpleStyleableObjectProperty/SimpleStyleableObjectProperty
date: 2021-01-11
key: JavaJava.S.SimpleStyleableObjectProperty
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleStyleableObjectProperty.constructores valor="SimpleStyleableObjectProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleStyleableObjectProperty(CssMetaData<? extends Styleable,T> cssMetaData)
public SimpleStyleableObjectProperty(CssMetaData<? extends Styleable,T> cssMetaData, Object bean, String name)
public SimpleStyleableObjectProperty(CssMetaData<? extends Styleable,T> cssMetaData, Object bean, String name, T initialValue)
public SimpleStyleableObjectProperty(CssMetaData<? extends Styleable,T> cssMetaData, T initialValue)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **T initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="T initialValue" %}
* **CssMetaData&lt;? extends Styleable**,  {% include w3api/param_description.html metodo=_dato parametro="CssMetaData<? extends Styleable" %}
* **Object bean**,  {% include w3api/param_description.html metodo=_dato parametro="Object bean" %}
* **T&gt; cssMetaData**,  {% include w3api/param_description.html metodo=_dato parametro="T> cssMetaData" %}

## Clase Padre
[SimpleStyleableObjectProperty](/Java/SimpleStyleableObjectProperty/)

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
