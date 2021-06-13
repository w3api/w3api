---
title: SimpleStringProperty.SimpleStringProperty()
permalink: /Java/SimpleStringProperty/SimpleStringProperty/
date: 2021-01-11
key: Java.S.SimpleStringProperty
category: Java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleStringProperty.constructores valor="SimpleStringProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleStringProperty()
public SimpleStringProperty(Object bean, String name)
public SimpleStringProperty(Object bean, String name, String initialValue)
public SimpleStringProperty(String initialValue)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Object bean**,  {% include w3api/param_description.html metodo=_dato parametro="Object bean" %}
* **String initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="String initialValue" %}

## Clase Padre
[SimpleStringProperty](/Java/SimpleStringProperty/)

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
