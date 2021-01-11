---
title: SimpleStyleableStringProperty.SimpleStyleableStringProperty()
permalink: Java/SimpleStyleableStringProperty/SimpleStyleableStringProperty
date: 2021-01-11
key: JavaJava.S.SimpleStyleableStringProperty
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleStyleableStringProperty.constructores valor="SimpleStyleableStringProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleStyleableStringProperty(CssMetaData<? extends Styleable,String> cssMetaData)
public SimpleStyleableStringProperty(CssMetaData<? extends Styleable,String> cssMetaData, Object bean, String name)
public SimpleStyleableStringProperty(CssMetaData<? extends Styleable,String> cssMetaData, Object bean, String name, String initialValue)
public SimpleStyleableStringProperty(CssMetaData<? extends Styleable,String> cssMetaData, String initialValue)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String&gt; cssMetaData**,  {% include w3api/param_description.html metodo=_dato parametro="String> cssMetaData" %}
* **CssMetaData&lt;? extends Styleable**,  {% include w3api/param_description.html metodo=_dato parametro="CssMetaData<? extends Styleable" %}
* **Object bean**,  {% include w3api/param_description.html metodo=_dato parametro="Object bean" %}
* **String initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="String initialValue" %}

## Clase Padre
[SimpleStyleableStringProperty](/Java/SimpleStyleableStringProperty/)

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
