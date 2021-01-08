---
title: SimpleSetProperty.SimpleSetProperty()
permalink: Java/SimpleSetProperty/SimpleSetProperty
date: 2021-01-04
key: JavaJava.S.SimpleSetProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleSetProperty.constructores valor="SimpleSetProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleSetProperty()
public SimpleSetProperty(Object bean, String name)
public SimpleSetProperty(Object bean, String name, ObservableSet<E> initialValue)
public SimpleSetProperty(ObservableSet<E> initialValue)
~~~

## Parámetros
* **Object bean**,  {% include w3api/param_description.html metodo=_data parametro="Object bean" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **ObservableSet&lt;E&gt; initialValue**,  {% include w3api/param_description.html metodo=_data parametro="ObservableSet<E> initialValue" %}

## Clase Padre
[SimpleSetProperty](/Java/SimpleSetProperty/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleSetProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
