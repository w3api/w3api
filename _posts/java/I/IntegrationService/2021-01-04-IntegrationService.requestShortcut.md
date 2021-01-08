---
title: IntegrationService.requestShortcut()
permalink: Java/IntegrationService/requestShortcut
date: 2021-01-04
key: JavaJava.I.IntegrationService
category: java
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
* **String submenu**,  {% include w3api/param_description.html metodo=_data parametro="String submenu" %}
* **boolean menu**,  {% include w3api/param_description.html metodo=_data parametro="boolean menu" %}
* **boolean desktop**,  {% include w3api/param_description.html metodo=_data parametro="boolean desktop" %}

## Clase Padre
[IntegrationService](/Java/IntegrationService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IntegrationService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
