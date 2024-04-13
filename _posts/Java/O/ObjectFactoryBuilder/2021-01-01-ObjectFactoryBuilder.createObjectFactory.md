---
title: ObjectFactoryBuilder.createObjectFactory()
permalink: /Java/ObjectFactoryBuilder/createObjectFactory/
date: 2021-01-11
key: Java.O.ObjectFactoryBuilder
category: Java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectFactoryBuilder.metodos valor="createObjectFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ObjectFactory createObjectFactory(Object obj, Hashtable<?,?> environment) throws NamingException
~~~

## Parámetros
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[ObjectFactoryBuilder](/Java/ObjectFactoryBuilder/)

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
