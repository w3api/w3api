---
title: PersistenceDelegate.writeObject()
permalink: /Java/PersistenceDelegate/writeObject/
date: 2021-01-11
key: Java.P.PersistenceDelegate
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PersistenceDelegate.metodos valor="writeObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeObject(Object oldInstance, Encoder out)
~~~

## Parámetros
* **Encoder out**,  {% include w3api/param_description.html metodo=_dato parametro="Encoder out" %}
* **Object oldInstance**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldInstance" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PersistenceDelegate](/Java/PersistenceDelegate/)

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
