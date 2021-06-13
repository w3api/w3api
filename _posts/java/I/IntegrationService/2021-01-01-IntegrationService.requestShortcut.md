---
title: IntegrationService.requestShortcut()
permalink: /Java/IntegrationService/requestShortcut/
date: 2021-01-11
key: Java.I.IntegrationService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', '6.0.18']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntegrationService.metodos valor="requestShortcut" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean requestShortcut(boolean desktop, boolean menu, String submenu)
~~~

## Parámetros
* **boolean desktop**,  {% include w3api/param_description.html metodo=_dato parametro="boolean desktop" %}
* **boolean menu**,  {% include w3api/param_description.html metodo=_dato parametro="boolean menu" %}
* **String submenu**,  {% include w3api/param_description.html metodo=_dato parametro="String submenu" %}

## Clase Padre
[IntegrationService](/Java/IntegrationService/)

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
