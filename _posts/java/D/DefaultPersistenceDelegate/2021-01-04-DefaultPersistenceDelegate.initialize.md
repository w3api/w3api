---
title: DefaultPersistenceDelegate.initialize()
permalink: Java/DefaultPersistenceDelegate/initialize
date: 2021-01-04
key: JavaJava.D.DefaultPersistenceDelegate
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultPersistenceDelegate.metodos valor="initialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void initialize(Class<?> type, Object oldInstance, Object newInstance, Encoder out)
~~~

## Parámetros
* **Object newInstance**,  {% include w3api/param_description.html metodo=_data parametro="Object newInstance" %}
* **Object oldInstance**,  {% include w3api/param_description.html metodo=_data parametro="Object oldInstance" %}
* **Encoder out**,  {% include w3api/param_description.html metodo=_data parametro="Encoder out" %}
* **Class&lt;?&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> type" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DefaultPersistenceDelegate](/Java/DefaultPersistenceDelegate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultPersistenceDelegate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
