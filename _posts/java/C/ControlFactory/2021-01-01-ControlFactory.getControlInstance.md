---
title: ControlFactory.getControlInstance()
permalink: /Java/ControlFactory/getControlInstance/
date: 2021-01-11
key: Java.C.ControlFactory
category: Java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ControlFactory.metodos valor="getControlInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Control getControlInstance(Control ctl) throws NamingException
public static Control getControlInstance(Control ctl, Context ctx, Hashtable<?,?> env) throws NamingException
~~~

## Parámetros
* **Context ctx**,  {% include w3api/param_description.html metodo=_dato parametro="Context ctx" %}
* **Hashtable&lt;?**,  {% include w3api/param_description.html metodo=_dato parametro="Hashtable<?" %}
* **?&gt; env**,  {% include w3api/param_description.html metodo=_dato parametro="?> env" %}
* **Control ctl**,  {% include w3api/param_description.html metodo=_dato parametro="Control ctl" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[ControlFactory](/Java/ControlFactory/)

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
