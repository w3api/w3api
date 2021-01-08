---
title: StateFactory.getStateToBind()
permalink: Java/StateFactory/getStateToBind
date: 2021-01-04
key: JavaJava.S.StateFactory
category: java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StateFactory.metodos valor="getStateToBind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getStateToBind(Object obj, Name name, Context nameCtx, Hashtable<?,?> environment) throws NamingException
~~~

## Parámetros
* **Context nameCtx**,  {% include w3api/param_description.html metodo=_data parametro="Context nameCtx" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}
* **?&gt; environment**,  {% include w3api/param_description.html metodo=_data parametro="?> environment" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_data parametro="Hashtable<?" %}
* **Name name**,  {% include w3api/param_description.html metodo=_data parametro="Name name" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[StateFactory](/Java/StateFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StateFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
