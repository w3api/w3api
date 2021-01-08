---
title: SimpleObjectProperty.SimpleObjectProperty()
permalink: Java/SimpleObjectProperty/SimpleObjectProperty
date: 2021-01-04
key: JavaJava.S.SimpleObjectProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleObjectProperty.constructores valor="SimpleObjectProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleObjectProperty()
public SimpleObjectProperty(Object bean, String name)
public SimpleObjectProperty(Object bean, String name, T initialValue)
public SimpleObjectProperty(T initialValue)
~~~

## Parámetros
* **Object bean**,  {% include w3api/param_description.html metodo=_data parametro="Object bean" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **T initialValue**,  {% include w3api/param_description.html metodo=_data parametro="T initialValue" %}

## Clase Padre
[SimpleObjectProperty](/Java/SimpleObjectProperty/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleObjectProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
