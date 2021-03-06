---
title: InitialContextFactoryBuilder.createInitialContextFactory()
permalink: /Java/InitialContextFactoryBuilder/createInitialContextFactory/
date: 2021-01-11
key: Java.I.InitialContextFactoryBuilder
category: Java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InitialContextFactoryBuilder.metodos valor="createInitialContextFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
InitialContextFactory createInitialContextFactory(Hashtable<?,?> environment) throws NamingException
~~~

## Parámetros
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[InitialContextFactoryBuilder](/Java/InitialContextFactoryBuilder/)

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
