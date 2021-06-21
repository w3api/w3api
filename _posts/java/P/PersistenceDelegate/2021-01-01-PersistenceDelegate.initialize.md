---
title: PersistenceDelegate.initialize()
permalink: /Java/PersistenceDelegate/initialize/
date: 2021-01-11
key: Java.P.PersistenceDelegate
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PersistenceDelegate.metodos valor="initialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void initialize(Class<?> type, Object oldInstance, Object newInstance, Encoder out)
~~~

## Parámetros
* **Class&lt;?&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> type" %}
* **Encoder out**,  {% include w3api/param_description.html metodo=_dato parametro="Encoder out" %}
* **Object newInstance**,  {% include w3api/param_description.html metodo=_dato parametro="Object newInstance" %}
* **Object oldInstance**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldInstance" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PersistenceDelegate](/Java/PersistenceDelegate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
