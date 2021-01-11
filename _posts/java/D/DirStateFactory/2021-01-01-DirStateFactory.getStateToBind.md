---
title: DirStateFactory.getStateToBind()
permalink: Java/DirStateFactory/getStateToBind
date: 2021-01-11
key: JavaJava.D.DirStateFactory
category: java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirStateFactory.metodos valor="getStateToBind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DirStateFactory.Result getStateToBind(Object obj, Name name, Context nameCtx, Hashtable<?,?> environment, Attributes inAttrs) throws NamingException
~~~

## Parámetros
* **Context nameCtx**,  {% include w3api/param_description.html metodo=_dato parametro="Context nameCtx" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **Attributes inAttrs**,  {% include w3api/param_description.html metodo=_dato parametro="Attributes inAttrs" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_dato parametro="?> environment" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[DirStateFactory](/Java/DirStateFactory/)

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
