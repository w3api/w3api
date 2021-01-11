---
title: DirectoryManager.getObjectInstance()
permalink: Java/DirectoryManager/getObjectInstance
date: 2021-01-11
key: JavaJava.D.DirectoryManager
category: java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectoryManager.metodos valor="getObjectInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Object getObjectInstance(Object refInfo, Name name, Context nameCtx, Hashtable<?,?> environment, Attributes attrs) throws Exception
~~~

## Parámetros
* **Context nameCtx**,  {% include w3api/param_description.html metodo=_dato parametro="Context nameCtx" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **Object refInfo**,  {% include w3api/param_description.html metodo=_dato parametro="Object refInfo" %}
* **Attributes attrs**,  {% include w3api/param_description.html metodo=_dato parametro="Attributes attrs" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}

## Excepciones
[Exception](/Java/Exception/), [NamingException](/Java/NamingException/)

## Clase Padre
[DirectoryManager](/Java/DirectoryManager/)

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
