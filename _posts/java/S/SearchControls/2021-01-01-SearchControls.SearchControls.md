---
title: SearchControls.SearchControls()
permalink: /Java/SearchControls/SearchControls/
date: 2021-01-11
key: Java.S.SearchControls
category: Java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SearchControls.constructores valor="SearchControls" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SearchControls()
public SearchControls(int scope, long countlim, int timelim, String[] attrs, boolean retobj, boolean deref)
~~~

## Parámetros
* **boolean deref**,  {% include w3api/param_description.html metodo=_dato parametro="boolean deref" %}
* **long countlim**,  {% include w3api/param_description.html metodo=_dato parametro="long countlim" %}
* **int timelim**,  {% include w3api/param_description.html metodo=_dato parametro="int timelim" %}
* **boolean retobj**,  {% include w3api/param_description.html metodo=_dato parametro="boolean retobj" %}
* **int scope**,  {% include w3api/param_description.html metodo=_dato parametro="int scope" %}
* **String[] attrs**,  {% include w3api/param_description.html metodo=_dato parametro="String[] attrs" %}

## Clase Padre
[SearchControls](/Java/SearchControls/)

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
