---
title: DefaultPersistenceDelegate.instantiate()
permalink: Java/DefaultPersistenceDelegate/instantiate
date: 2021-01-11
key: JavaJava.D.DefaultPersistenceDelegate
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultPersistenceDelegate.metodos valor="instantiate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Expression instantiate(Object oldInstance, Encoder out)
~~~

## Parámetros
* **Encoder out**,  {% include w3api/param_description.html metodo=_dato parametro="Encoder out" %}
* **Object oldInstance**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldInstance" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
