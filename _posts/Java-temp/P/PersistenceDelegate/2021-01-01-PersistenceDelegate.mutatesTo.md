---
title: PersistenceDelegate.mutatesTo()
permalink: /Java/PersistenceDelegate/mutatesTo/
date: 2021-01-11
key: Java.P.PersistenceDelegate
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PersistenceDelegate.metodos valor="mutatesTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean mutatesTo(Object oldInstance, Object newInstance)
~~~

## Parámetros
* **Object newInstance**,  {% include w3api/param_description.html metodo=_dato parametro="Object newInstance" %}
* **Object oldInstance**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldInstance" %}

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
