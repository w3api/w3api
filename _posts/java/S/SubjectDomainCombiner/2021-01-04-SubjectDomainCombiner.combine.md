---
title: SubjectDomainCombiner.combine()
permalink: Java/SubjectDomainCombiner/combine
date: 2021-01-04
key: JavaJava.S.SubjectDomainCombiner
category: java
tags: ['java se', 'javax.security.auth', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SubjectDomainCombiner.metodos valor="combine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ProtectionDomain[] combine(ProtectionDomain[] currentDomains, ProtectionDomain[] assignedDomains)
~~~

## Parámetros
* **ProtectionDomain[] currentDomains**,  {% include w3api/param_description.html metodo=_data parametro="ProtectionDomain[] currentDomains" %}
* **ProtectionDomain[] assignedDomains**,  {% include w3api/param_description.html metodo=_data parametro="ProtectionDomain[] assignedDomains" %}

## Clase Padre
[SubjectDomainCombiner](/Java/SubjectDomainCombiner/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SubjectDomainCombiner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
