---
title: GSSManager.addProviderAtFront()
permalink: Java/GSSManager/addProviderAtFront
date: 2021-01-11
key: JavaJava.G.GSSManager
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSManager.metodos valor="addProviderAtFront" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void addProviderAtFront(Provider p, Oid mech) throws GSSException
~~~

## Parámetros
* **Provider p**,  {% include w3api/param_description.html metodo=_dato parametro="Provider p" %}
* **Oid mech**,  {% include w3api/param_description.html metodo=_dato parametro="Oid mech" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[GSSManager](/Java/GSSManager/)

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