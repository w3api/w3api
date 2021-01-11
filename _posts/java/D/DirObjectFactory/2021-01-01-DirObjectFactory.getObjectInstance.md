---
title: DirObjectFactory.getObjectInstance()
permalink: Java/DirObjectFactory/getObjectInstance
date: 2021-01-11
key: JavaJava.D.DirObjectFactory
category: java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirObjectFactory.metodos valor="getObjectInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getObjectInstance(Object obj, Name name, Context nameCtx, Hashtable<?,?> environment, Attributes attrs) throws Exception
~~~

## Parámetros
* **Context nameCtx**,  {% include w3api/param_description.html metodo=_dato parametro="Context nameCtx" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **Attributes attrs**,  {% include w3api/param_description.html metodo=_dato parametro="Attributes attrs" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}

## Excepciones
[Exception](/Java/Exception/)

## Clase Padre
[DirObjectFactory](/Java/DirObjectFactory/)

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
