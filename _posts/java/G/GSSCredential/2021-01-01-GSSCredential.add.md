---
title: GSSCredential.add()
permalink: /Java/GSSCredential/add/
date: 2021-01-11
key: Java.G.GSSCredential
category: Java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSCredential.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void add(GSSName name, int initLifetime, int acceptLifetime, Oid mech, int usage) throws GSSException
~~~

## Parámetros
* **int initLifetime**,  {% include w3api/param_description.html metodo=_dato parametro="int initLifetime" %}
* **int acceptLifetime**,  {% include w3api/param_description.html metodo=_dato parametro="int acceptLifetime" %}
* **Oid mech**,  {% include w3api/param_description.html metodo=_dato parametro="Oid mech" %}
* **int usage**,  {% include w3api/param_description.html metodo=_dato parametro="int usage" %}
* **GSSName name**,  {% include w3api/param_description.html metodo=_dato parametro="GSSName name" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[GSSCredential](/Java/GSSCredential/)

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
