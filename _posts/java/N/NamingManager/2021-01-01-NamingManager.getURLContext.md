---
title: NamingManager.getURLContext()
permalink: /Java/NamingManager/getURLContext/
date: 2021-01-11
key: Java.N.NamingManager
category: Java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamingManager.metodos valor="getURLContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Context getURLContext(String scheme, Hashtable<?,?> environment) throws NamingException
~~~

## Parámetros
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}
* **String scheme**,  {% include w3api/param_description.html metodo=_dato parametro="String scheme" %}

## Excepciones
[NamingException](/Java/NamingException/)

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
