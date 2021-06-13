---
title: NamingManager.getInitialContext()
permalink: Java/NamingManager/getInitialContext
date: 2021-01-11
key: JavaJava.N.NamingManager
category: Java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamingManager.metodos valor="getInitialContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Context getInitialContext(Hashtable<?,?> env) throws NamingException
~~~

## Parámetros
* **?&gt; env**,  {% include w3api/param_description.html metodo=_dato parametro="?> env" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}

## Excepciones
[NamingException](/Java/NamingException/), [NoInitialContextException](/Java/NoInitialContextException/)

## Clase Padre
[NamingManager](/Java/NamingManager/)

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
