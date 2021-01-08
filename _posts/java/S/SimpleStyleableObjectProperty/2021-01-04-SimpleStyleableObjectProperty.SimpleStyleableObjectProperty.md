---
title: SimpleStyleableObjectProperty.SimpleStyleableObjectProperty()
permalink: Java/SimpleStyleableObjectProperty/SimpleStyleableObjectProperty
date: 2021-01-04
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
* **T&gt; cssMetaData**,  {% include w3api/param_description.html metodo=_data parametro="T> cssMetaData" %}
* **Object bean**,  {% include w3api/param_description.html metodo=_data parametro="Object bean" %}
* **T initialValue**,  {% include w3api/param_description.html metodo=_data parametro="T initialValue" %}
* **CssMetaData&lt;? extends Styleable**,  {% include w3api/param_description.html metodo=_data parametro="CssMetaData<? extends Styleable" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[SimpleStyleableObjectProperty](/Java/SimpleStyleableObjectProperty/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleStyleableObjectProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
