---
title: SearchControls.SearchControls()
permalink: Java/SearchControls/SearchControls
date: 2021-01-04
key: JavaJava.S.SearchControls
category: java
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
* **int scope**,  {% include w3api/param_description.html metodo=_data parametro="int scope" %}
* **long countlim**,  {% include w3api/param_description.html metodo=_data parametro="long countlim" %}
* **int timelim**,  {% include w3api/param_description.html metodo=_data parametro="int timelim" %}
* **String[] attrs**,  {% include w3api/param_description.html metodo=_data parametro="String[] attrs" %}
* **boolean deref**,  {% include w3api/param_description.html metodo=_data parametro="boolean deref" %}
* **boolean retobj**,  {% include w3api/param_description.html metodo=_data parametro="boolean retobj" %}

## Clase Padre
[SearchControls](/Java/SearchControls/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SearchControls.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
