---
title: InitialContextFactory.getInitialContext()
permalink: /Java/InitialContextFactory/getInitialContext/
date: 2021-01-11
key: Java.I.InitialContextFactory
category: Java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InitialContextFactory.metodos valor="getInitialContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Context getInitialContext(Hashtable<?,?> environment) throws NamingException
~~~

## Parámetros
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[InitialContextFactory](/Java/InitialContextFactory/)

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
