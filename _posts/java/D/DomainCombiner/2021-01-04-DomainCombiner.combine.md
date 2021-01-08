---
title: DomainCombiner.combine()
permalink: Java/DomainCombiner/combine
date: 2021-01-04
key: JavaJava.D.DomainCombiner
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DomainCombiner.metodos valor="combine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ProtectionDomain[] combine(ProtectionDomain[] currentDomains, ProtectionDomain[] assignedDomains)
~~~

## Parámetros
* **ProtectionDomain[] currentDomains**,  {% include w3api/param_description.html metodo=_data parametro="ProtectionDomain[] currentDomains" %}
* **ProtectionDomain[] assignedDomains**,  {% include w3api/param_description.html metodo=_data parametro="ProtectionDomain[] assignedDomains" %}

## Clase Padre
[DomainCombiner](/Java/DomainCombiner/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DomainCombiner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
